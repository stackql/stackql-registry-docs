---
title: hosted_configuration_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_configuration_versions
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>hosted_configuration_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_configuration_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hosted_configuration_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appconfig.hosted_configuration_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>configuration_profile_id</code></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><code>version_number</code></td><td><code>string</code></td><td>Current version number of hosted configuration version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>hosted_configuration_versions</code> resource, the following permissions are required:

### Create
```json
appconfig:CreateHostedConfigurationVersion
```

### List
```json
appconfig:ListHostedConfigurationVersions
```


## Example
```sql
SELECT
region,
application_id,
configuration_profile_id,
version_number
FROM awscc.appconfig.hosted_configuration_versions
WHERE region = 'us-east-1'
```
