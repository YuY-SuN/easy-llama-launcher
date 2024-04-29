#!/usr/bin/env python3

"""
DI configuration
"""
from repository import Session
from repository.llm_repository import LLMRepository
from service.llm_service import LLMService
from dto.llm_dto import LLMDTO
session = Session()
repository = LLMRepository(session)
service = LLMService(repository)

"""
main process
"""
if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest="command", required=True, help="DLかサーバ起動かの選択")

    parser_download = subparser.add_parser("download", help="huggingfaceからモデルのダウンロード")
    parser_download.add_argument("-c", "--chat-template", required=True,help="chat templateのnamespace ex) microsoft/Phi-3-mini-128k-instruct")
    parser_download.add_argument("-n", "--namespace",     required=True,help="ダウンロードするnamespace ex) mmnga/Phi-3-mini-128k-instruct-gguf")
    parser_download.add_argument("-m", "--modelname",      required=True,help="ダウンロードするファイル名 ex) Phi-3-mini-128k-instruct-Q4_K_M.gguf")
    parser_download.add_argument("-k", "--nickname",      help="このモデルを管理するためのニックネーム")

    parser_server = subparser.add_parser("server", help="serverの起動")
    parser_server.add_argument("-k", "--nickname", required=True, help="起動するモデル名、またはnickname")

    args = parser.parse_args()

    if args.command == "download":
        service.download_model( LLMDTO(  namespace=args.namespace
                                      ,  chat_template=args.chat_template
                                      ,  model_name=args.modelname
                                      ,  nickname=args.nickname if args.nickname else args.modelname) )
    elif args.command == "server":
        service.start_server(args.nickname)
