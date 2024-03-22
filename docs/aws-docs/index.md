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
image: /img/providers/aws/stackql-aws-provider-featured-image.png
id: aws-doc
slug: /providers/aws

---
EC2, IAM and S3 core AWS Services.
:::tip

All AWS Services (incl Lambda, DynamoDB, RDS, etc) are supported by the [__`awscc`__](https://awscc.stackql.io/providers/awscc/) (AWS Cloud Control API) provider in StackQL.

:::      
        
    
:::info Provider Summary (v24.03.00216)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>4</b></span><br />
<span>total methods:&nbsp;<b>780</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>346</b></span><br />
<span>total selectable resources:&nbsp;<b>250</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `aws` provider, run the following command:  

```bash
REGISTRY PULL aws;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `AWS_ACCESS_KEY_ID` - AWS Access Key ID (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SECRET_ACCESS_KEY` - AWS Secret Access Key (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SESSION_TOKEN` - [__OPTIONAL:__ only required if using `aws sts assume-role`] AWS Session Token (see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "aws": { "type": "aws_signing_v4", "keyIDenvvar": "YOUR_ACCESS_KEY_ID_VAR", "credentialsenvvar": "YOUR_SECRET_KEY_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'keyIDenvvar': 'YOUR_ACCESS_KEY_ID_VAR', 'credentialsenvvar': 'YOUR_SECRET_KEY_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Server Parameters


The following parameter is required for the `aws` provider:  

- `region` - AWS region (e.g. `us-east-1`)

This parameter must be supplied to the `WHERE` clause of each `SELECT` statement.
    
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
