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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>hosted_configuration_version</code> resource or lists <code>hosted_configuration_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_configuration_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::HostedConfigurationVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.hosted_configuration_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the hosted configuration version.</td></tr>
<tr><td><CopyableCode code="content_type" /></td><td><code>string</code></td><td>A standard MIME type describing the format of the configuration content.</td></tr>
<tr><td><CopyableCode code="latest_version_number" /></td><td><code>integer</code></td><td>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The content of the configuration or the configuration data.</td></tr>
<tr><td><CopyableCode code="version_label" /></td><td><code>string</code></td><td>A user-defined label for an AWS AppConfig hosted configuration version.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="version_number" /></td><td><code>string</code></td><td>Current version number of hosted configuration version.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html"><code>AWS::AppConfig::HostedConfigurationVersion</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ApplicationId, ConfigurationProfileId, Content, ContentType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>hosted_configuration_versions</code> in a region.
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
FROM aws.appconfig.hosted_configuration_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>hosted_configuration_version</code>.
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
FROM aws.appconfig.hosted_configuration_versions
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<ConfigurationProfileId>|<VersionNumber>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hosted_configuration_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.appconfig.hosted_configuration_versions (
 ConfigurationProfileId,
 ContentType,
 Content,
 ApplicationId,
 region
)
SELECT 
'{{ ConfigurationProfileId }}',
 '{{ ContentType }}',
 '{{ Content }}',
 '{{ ApplicationId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.hosted_configuration_versions (
 ConfigurationProfileId,
 Description,
 ContentType,
 LatestVersionNumber,
 Content,
 VersionLabel,
 ApplicationId,
 region
)
SELECT 
 '{{ ConfigurationProfileId }}',
 '{{ Description }}',
 '{{ ContentType }}',
 '{{ LatestVersionNumber }}',
 '{{ Content }}',
 '{{ VersionLabel }}',
 '{{ ApplicationId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: hosted_configuration_version
    props:
      - name: ConfigurationProfileId
        value: '{{ ConfigurationProfileId }}'
      - name: Description
        value: '{{ Description }}'
      - name: ContentType
        value: '{{ ContentType }}'
      - name: LatestVersionNumber
        value: '{{ LatestVersionNumber }}'
      - name: Content
        value: '{{ Content }}'
      - name: VersionLabel
        value: '{{ VersionLabel }}'
      - name: ApplicationId
        value: '{{ ApplicationId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appconfig.hosted_configuration_versions
WHERE data__Identifier = '<ApplicationId|ConfigurationProfileId|VersionNumber>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hosted_configuration_versions</code> resource, the following permissions are required:

### Read
```json
appconfig:GetHostedConfigurationVersion
```

### Create
```json
appconfig:CreateHostedConfigurationVersion
```

### List
```json
appconfig:ListHostedConfigurationVersions
```

### Delete
```json
appconfig:DeleteHostedConfigurationVersion
```
