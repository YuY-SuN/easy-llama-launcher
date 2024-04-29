#!/usr/bin/env python3

import repository
from model import llm


llm.Base.metadata.create_all(repository.engine)
