# Copyright (C) 2021 Wind River Systems, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# from datetime import datetime
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    # Integer,
    String,
    # Date,
    DateTime,
    # engine,
    # ForeignKey,
    # event,
    Enum
)

# from sqlalchemy.orm import mapper

# from o2ims.domain import stx_object as ocloudModel

from o2common.service.unit_of_work import AbstractUnitOfWork
# from o2ims.adapter.unit_of_work import SqlAlchemyUnitOfWork
from o2ims.domain.resource_type import ResourceTypeEnum

from o2common.helper import o2logging
logger = o2logging.get_logger(__name__)

metadata = MetaData()

stxobject = Table(
    "stxcache",
    metadata,
    Column("id", String(255), primary_key=True),
    Column("type", Enum(ResourceTypeEnum, native_enum=False)),
    Column("name", String(255)),
    Column("updatetime", DateTime),
    Column("createtime", DateTime),
    Column("hash", String(255)),
    Column("content", String)
)


def start_o2ims_stx_mappers(uow: AbstractUnitOfWork):
    return
    # logger.info("Starting O2 IMS Stx mappers")
    # mapper(ocloudModel.StxGenericModel, stxobject)

    # with uow:
    #     engine1 = uow.session.get_bind()
    #     metadata.create_all(engine1)
    #     uow.commit()
