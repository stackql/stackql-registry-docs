---
title: source_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_locations
  - mediatailor
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

Creates, updates, deletes or gets a <code>source_location</code> resource or lists <code>source_locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::SourceLocation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.source_locations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_configuration" /></td><td><code>object</code></td><td><p>Access configuration parameters.</p></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the source location.</p></td></tr>
<tr><td><CopyableCode code="default_segment_delivery_configuration" /></td><td><code>object</code></td><td><p>The optional configuration for a server that serves segments. Use this if you want the segment delivery server to be different from the source location server. For example, you can configure your source location server to be an origination server, such as MediaPackage, and the segment delivery server to be a content delivery network (CDN), such as CloudFront. If you don't specify a segment delivery server, then the source location server is used.</p></td></tr>
<tr><td><CopyableCode code="http_configuration" /></td><td><code>object</code></td><td><p>The HTTP configuration for the source location.</p></td></tr>
<tr><td><CopyableCode code="segment_delivery_configurations" /></td><td><code>array</code></td><td><p>A list of the segment delivery configurations associated with this resource.</p></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the source location.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html"><code>AWS::MediaTailor::SourceLocation</code></a>.

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
    <td><CopyableCode code="HttpConfiguration, SourceLocationName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>source_locations</code> in a region.
```sql
SELECT
region,
access_configuration,
arn,
default_segment_delivery_configuration,
http_configuration,
segment_delivery_configurations,
source_location_name,
tags
FROM aws.mediatailor.source_locations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>source_location</code>.
```sql
SELECT
region,
access_configuration,
arn,
default_segment_delivery_configuration,
http_configuration,
segment_delivery_configurations,
source_location_name,
tags
FROM aws.mediatailor.source_locations
WHERE region = 'us-east-1' AND data__Identifier = '<SourceLocationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_location</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediatailor.source_locations (
 HttpConfiguration,
 SourceLocationName,
 region
)
SELECT 
'{{ HttpConfiguration }}',
 '{{ SourceLocationName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediatailor.source_locations (
 AccessConfiguration,
 DefaultSegmentDeliveryConfiguration,
 HttpConfiguration,
 SegmentDeliveryConfigurations,
 SourceLocationName,
 Tags,
 region
)
SELECT 
 '{{ AccessConfiguration }}',
 '{{ DefaultSegmentDeliveryConfiguration }}',
 '{{ HttpConfiguration }}',
 '{{ SegmentDeliveryConfigurations }}',
 '{{ SourceLocationName }}',
 '{{ Tags }}',
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
  - name: source_location
    props:
      - name: AccessConfiguration
        value:
          AccessType: '{{ AccessType }}'
          SecretsManagerAccessTokenConfiguration:
            HeaderName: '{{ HeaderName }}'
            SecretArn: '{{ SecretArn }}'
            SecretStringKey: '{{ SecretStringKey }}'
      - name: DefaultSegmentDeliveryConfiguration
        value:
          BaseUrl: '{{ BaseUrl }}'
      - name: HttpConfiguration
        value:
          BaseUrl: '{{ BaseUrl }}'
      - name: SegmentDeliveryConfigurations
        value:
          - BaseUrl: '{{ BaseUrl }}'
            Name: '{{ Name }}'
      - name: SourceLocationName
        value: '{{ SourceLocationName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediatailor.source_locations
WHERE data__Identifier = '<SourceLocationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>source_locations</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateSourceLocation,
mediatailor:DescribeSourceLocation,
mediatailor:TagResource,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
kms:CreateGrant
```

### Read
```json
mediatailor:DescribeSourceLocation
```

### Update
```json
mediatailor:DescribeSourceLocation,
mediatailor:TagResource,
mediatailor:UntagResource,
mediatailor:UpdateSourceLocation,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
kms:CreateGrant
```

### Delete
```json
mediatailor:DeleteSourceLocation,
mediatailor:DescribeSourceLocation
```

### List
```json
mediatailor:ListSourceLocations
```
