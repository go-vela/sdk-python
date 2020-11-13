These are the bits used to generate the SDK from the Swagger spec.

To do this, you need to have the https://github.com/go-vela/server repo cloned:

Then ensure you have the swagger-codegen command installed:

`brew install swagger-codegen`

(Or use some other method)

Then run:

`swagger-codegen generate -c config.json -l python -i vela.json -o vela
find vela -name \*.py -exec sed -i 's/# coding: utf-8/# coding: utf-8\n#\n# Copyright (c) 2020 Target Brands, Inc. All rights reserved./' \{\} +`

