---
title: aws
hide_title: false
hide_table_of_contents: false
keywords:
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.pngx
id: aws-doc
slug: /providers/aws
---
Cloud services from AWS.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL aws v0.1.3;
```

## Authentication
```javascript

{
    "aws": {
     /**
      * Type of authentication to use, suported values include:  aws_signing_v4
      * @type String
      */
     "type": string, 
     /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
     "credentialsenvvar": string,
     /**
      * Value of AWS_ACCESS_KEY_ID.
      * @type String
      */
     "keyID": string,      
    }
}

```
### Example (Mac/Linux)
```bash

AUTH="{ \"aws\": { \"type\": \"aws_signing_v4\", \"credentialsenvvar\": \"AWS_SECRET_ACCESS_KEY\", \"keyID\": \"${AWS_ACCESS_KEY_ID}\" }}"
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'credentialsenvvar': 'AWS_SECRET_ACCESS_KEY', 'keyID': '$Env.AWS_ACCESS_KEY_ID' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="provider-resources/cloud_control/">cloud_control</a><br />
<a href="provider-resources/ec2/">ec2</a><br />
</div>
<div class="providerDocColumn">
<a href="provider-resources/s3/">s3</a><br />
</div>
</div>



