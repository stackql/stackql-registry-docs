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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>hosted_configuration_version</code> resource, use <code>hosted_configuration_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_configuration_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::HostedConfigurationVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.hosted_configuration_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the hosted configuration version.</td></tr>
<tr><td><CopyableCode code="content_type" /></td><td><code>string</code></td><td>A standard MIME type describing the format of the configuration content.</td></tr>
<tr><td><CopyableCode code="latest_version_number" /></td><td><code>integer</code></td><td>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The content of the configuration or the configuration data.</td></tr>
<tr><td><CopyableCode code="version_label" /></td><td><code>string</code></td><td>A user-defined label for an AWS AppConfig hosted configuration version.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="version_number" /></td><td><code>string</code></td><td>Current version number of hosted configuration version.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
configuration_profile_id,
description,
content_type,
latest_version_number,
content,
version_label,
application_id,
version_number
FROM aws.appconfig.hosted_configuration_version
WHERE data__Identifier = '<ApplicationId>|<ConfigurationProfileId>|<VersionNumber>';
```

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

