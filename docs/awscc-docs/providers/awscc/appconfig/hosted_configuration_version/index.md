---
title: hosted_configuration_version
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_configuration_version
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
Gets an individual <code>hosted_configuration_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_configuration_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hosted_configuration_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appconfig.hosted_configuration_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>configuration_profile_id</code></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><code>version_number</code></td><td><code>string</code></td><td>Current version number of hosted configuration version.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the hosted configuration version.</td></tr>
<tr><td><code>content</code></td><td><code>string</code></td><td>The content of the configuration or the configuration data.</td></tr>
<tr><td><code>content_type</code></td><td><code>string</code></td><td>A standard MIME type describing the format of the configuration content.</td></tr>
<tr><td><code>latest_version_number</code></td><td><code>integer</code></td><td>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</td></tr>
<tr><td><code>version_label</code></td><td><code>string</code></td><td>A user-defined label for an AWS AppConfig hosted configuration version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>hosted_configuration_version</code> resource, the following permissions are required:

### Read
```json
appconfig:GetHostedConfigurationVersion
```

### Delete
```json
appconfig:DeleteHostedConfigurationVersion
```


## Example
```sql
SELECT
region,
application_id,
configuration_profile_id,
version_number,
description,
content,
content_type,
latest_version_number,
version_label
FROM awscc.appconfig.hosted_configuration_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationId&gt;'
AND data__Identifier = '&lt;ConfigurationProfileId&gt;'
AND data__Identifier = '&lt;VersionNumber&gt;'
```
