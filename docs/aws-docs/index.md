---
title: aws
hide_title: false
hide_table_of_contents: false
keywords:
  - aws
  - amazon web services
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
id: aws-doc
slug: /providers/aws

---
Cloud services from AWS.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>4</b></span><br />
<span>total methods:&nbsp;<b>780</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>344</b></span><br />
<span>total selectable resources:&nbsp;<b>248</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL aws v23.01.00108;
```

## Authentication
```javascript

{
  "aws": {
    "type": string, // authentication type to use, suported values:  aws_signing_v4
    "keyIDenvvar": string, // env var containing AWS_ACCESS_KEY_ID
    "credentialsenvvar": string, // env var containing AWS_SECRET_ACCESS_KEY
  }
}

```
### Example (Mac/Linux)
```bash

AUTH="{ "aws": { "type": "aws_signing_v4", "credentialsenvvar": "AWS_SECRET_ACCESS_KEY", "keyIDenvvar": "AWS_ACCESS_KEY_ID" }}"
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'credentialsenvvar': 'AWS_SECRET_ACCESS_KEY', 'keyIDenvvar': 'AWS_ACCESS_KEY_ID' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/aws/cloud_control/">cloud_control</a><br />
<a href="/providers/aws/ec2/">ec2</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/aws/iam/">iam</a><br />
<a href="/providers/aws/s3/">s3</a><br />
</div>
</div>
