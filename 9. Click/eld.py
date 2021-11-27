import json
import logging
import pandas
import click
import asyncio
import aiohttp

from functools import wraps
from datetime import datetime
# from eld_cli.factories import LoadEldProjectFromExcelServiceFactory
# from eld_cli.services import EldProjectReportToExcelService, EldRitsReportsApiService

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s',
                    encoding='utf-8', level=logging.INFO)

__version__ = "0.6.3-beta.1"


# LOCAL API ENDPOINT
#API_ENDPOINT = 'http://localhost:8000'

# STAGING API ENDPOINT
API_ENDPOINT = 'https://evaluador-ley-ductos-staging-dsr4vgyiua-uc.a.run.app'

# PRODUCTION API ENDPOINT
#API_ENDPOINT = 'https://evaluador-ley-ductos-dsr4vgyiua-uc.a.run.app'


# load_eld_project_from_excel_service_factory = LoadEldProjectFromExcelServiceFactory()
# eld_project_report_to_excel_service = EldProjectReportToExcelService()


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        return asyncio.run(f(*args, **kwargs))

    return wrapper


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except click.ClickException as cerr:
            print("cerr", cerr)
            return
        except Exception as err:
            logging.debug("Error", err)
            error_message = err.to_json(
            ) if kwargs["result_json"] else err.to_str()
            click.echo(error_message, err=True)
    return inner_function


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.command(name="json")
@click.argument("project-path", type=click.Path(exists=True))
@click.option("--catalog", "-c", type=click.Path(exists=True), default="./eld_project_catalog_example.xlsx", help="Eld Catalog Excel File Path")
@click.option("--path-out", "-o", type=click.Path(exists=True, file_okay=False), default=None, help="Path to Folder for save Project Excel File")
@click.option('--result-json', default=False, is_flag=True)
@exception_handler
def to_json(project_path, catalog, path_out, result_json):
    json_path_out = None if path_out == None else path_out.replace('\\', '/')
    if json_path_out == None:
        json_path_out_list = project_path.replace('\\', '/').split("/")
        json_path_out_list.pop()
        json_path_out = "/".join(json_path_out_list)
    logging.debug("Load excel project")
    eld_project_from_excel_service = load_eld_project_from_excel_service_factory.create_eld_project_from_excel_service(
        eld_project_input_file=project_path,
        eld_project_catalog_file=catalog)
    eld_project_dict = eld_project_from_excel_service()
    logging.debug("Create json project")
    with open(f'{json_path_out}\\project_{eld_project_dict["name"]}.json', 'w') as outfile:
        json.dump(eld_project_dict, outfile)
    if result_json:
        click.echo(json.dumps({"success": True}))


@cli.command(name="login")
@click.option("--endpoint", "-e", default=API_ENDPOINT, help="Cloud Endpoint")
@click.option("--username", "-u", required=True, help="Cloud Username")
@click.option("--password", "-p", required=True, help="Cloud Password")
@click.option('--result-json', default=False, is_flag=True)
@exception_handler
@coro
async def login(endpoint, username, password, result_json):
    eld_rits_reports_api_service = EldRitsReportsApiService(
        eld_project_report_to_excel_service=eld_project_report_to_excel_service,
        endpoint=endpoint)
    crendentials = {"username": username, "password": password}
    async with aiohttp.ClientSession() as session:
        await eld_rits_reports_api_service.login(
            session=session,
            crendentials=crendentials,
        )
        if result_json:
            click.echo(json.dumps({"success": True}))


@cli.command(name="project")
@click.argument("project-path", type=click.Path(exists=True))
@click.option("--catalog", "-c", type=click.Path(exists=True), default="./eld_project_catalog_example.xlsx", help="Project Catalog Excel File Path")
@click.option("--endpoint", "-e", default=API_ENDPOINT, help="Cloud Endpoint")
@click.option("--username", "-u", required=True, help="Cloud Username")
@click.option("--password", "-p", required=True, help="Cloud Password")
@click.option("--rits", "-r", type=click.Choice(['catv:backbones', 'catv:amplifiers', 'smatv:backbones', 'smatv:amplifiers', 'fo'], case_sensitive=False), default=("catv:backbones", "catv:amplifiers", "smatv:backbones", "smatv:backbones", "fo"), multiple=True, help="List of RITs to compute ex: -r catv -r smatv")
@click.option("--path-out", "-o", type=click.Path(exists=True, file_okay=False), default=None, help="Path to Folder for save Project Excel File")
@click.option('--result-json', default=False, is_flag=True)
@exception_handler
@coro
async def compute_eld_project(project_path, catalog, endpoint, username, password, rits, path_out, result_json):
    eld_rits_reports_api_service = EldRitsReportsApiService(
        eld_project_report_to_excel_service=eld_project_report_to_excel_service,
        endpoint=endpoint)
    excel_report_path_out = None if path_out == None else path_out.replace(
        '\\', '/')
    if excel_report_path_out == None:
        excel_report_path_out_list = project_path.replace('\\', '/').split("/")
        excel_report_path_out_list.pop()
        excel_report_path_out = "/".join(excel_report_path_out_list)
    eld_project_from_excel_service = load_eld_project_from_excel_service_factory.create_eld_project_from_excel_service(
        eld_project_input_file=project_path,
        eld_project_catalog_file=catalog)
    eld_project_dict = eld_project_from_excel_service()
    coroutines = []
    crendentials = {"username": username, "password": password}
    async with aiohttp.ClientSession() as session:
        if "catv:backbones" in rits:
            coroutines.append(
                eld_rits_reports_api_service.compute_catv_rit_report(
                    session=session,
                    crendentials=crendentials,
                    eld_project_dict=eld_project_dict,
                    rit_strategy="BACKBONES",
                    excel_report_path_out=excel_report_path_out
                )
            )
        if "catv:amplifiers" in rits:
            coroutines.append(
                eld_rits_reports_api_service.compute_catv_rit_report(
                    session=session,
                    crendentials=crendentials,
                    eld_project_dict=eld_project_dict,
                    rit_strategy="AMPLIFIERS",
                    excel_report_path_out=excel_report_path_out
                )
            )
        if "smatv:backbones" in rits:
            coroutines.append(
                eld_rits_reports_api_service.compute_smatv_rit_report(
                    session=session,
                    crendentials=crendentials,
                    eld_project_dict=eld_project_dict,
                    rit_strategy="BACKBONES",
                    excel_report_path_out=excel_report_path_out
                )
            )
        if "smatv:amplifiers" in rits:
            coroutines.append(
                eld_rits_reports_api_service.compute_smatv_rit_report(
                    session=session,
                    crendentials=crendentials,
                    eld_project_dict=eld_project_dict,
                    rit_strategy="AMPLIFIERS",
                    excel_report_path_out=excel_report_path_out
                )
            )
        if "fo" in rits:
            coroutines.append(
                eld_rits_reports_api_service.compute_fo_rit_report(
                    session=session,
                    crendentials=crendentials,
                    eld_project_dict=eld_project_dict,
                    excel_report_path_out=excel_report_path_out
                )
            )
        results = await asyncio.gather(*coroutines, return_exceptions=True)
    result_dict = {}
    rits_dict = {}
    report_name = f"{excel_report_path_out}/report_{eld_project_dict['name']}_{datetime.now().strftime('%Y-%m-%d %I-%M-%S')}.xlsx"
    has_valid_result = False
    for result in results:
        if "exception" in result.keys():
            result_dict[result["rit"]] = {
                "code": result["exception"].code, "message": result["exception"].message}
            continue
        if "result" in result.keys():
            if result["result"] == None:
                result_dict[result["rit"]] = False
                continue
            has_valid_result = True
            result_dict[result["rit"]] = True
            rits_dict[result["rit"]] = result["result"]
    if has_valid_result:
        with pandas.ExcelWriter(report_name) as writer:  # pylint: disable=abstract-class-instantiated
            eld_project_report_to_excel_service.make_eld_project_report(
                writer=writer,
                eld_project_dict=eld_project_dict,
                catv_rit_report_backbones_dict=rits_dict["catv:backbones"] if result_dict.get(
                    "catv:backbones") == True else None,
                catv_rit_report_amplifiers_dict=rits_dict["catv:amplifiers"] if result_dict.get(
                    "catv:amplifiers") == True else None,
                smatv_rit_report_backbones_dict=rits_dict["smatv:backbones"] if result_dict.get(
                    "smatv:backbones") == True else None,
                smatv_rit_report_amplifiers_dict=rits_dict["smatv:amplifiers"] if result_dict.get(
                    "smatv:amplifiers") == True else None,
                fo_rit_report_dict=rits_dict["fo"] if result_dict.get("fo") == True else None)
    if result_json:
        click.echo(json.dumps({"success": True, "data": result_dict}))


if __name__ == '__main__':
    cli()
