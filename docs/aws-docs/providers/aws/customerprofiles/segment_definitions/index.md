---
title: segment_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - segment_definitions
  - customerprofiles
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

Creates, updates, deletes or gets a <code>segment_definition</code> resource or lists <code>segment_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>segment_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A segment definition resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.segment_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this segment definition got created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the segment definition.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the segment definition.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="segment_definition_name" /></td><td><code>string</code></td><td>The unique name of the segment definition.</td></tr>
<tr><td><CopyableCode code="segment_groups" /></td><td><code>object</code></td><td>An array that defines the set of segment criteria to evaluate when handling segment groups for the segment.</td></tr>
<tr><td><CopyableCode code="segment_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the segment definition.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html"><code>AWS::CustomerProfiles::SegmentDefinition</code></a>.

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
    <td><CopyableCode code="DomainName, DisplayName, SegmentDefinitionName, SegmentGroups, region" /></td>
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
Gets all <code>segment_definitions</code> in a region.
```sql
SELECT
region,
created_at,
description,
display_name,
domain_name,
segment_definition_name,
segment_groups,
segment_definition_arn,
tags
FROM aws.customerprofiles.segment_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>segment_definition</code>.
```sql
SELECT
region,
created_at,
description,
display_name,
domain_name,
segment_definition_name,
segment_groups,
segment_definition_arn,
tags
FROM aws.customerprofiles.segment_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<SegmentDefinitionName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>segment_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.customerprofiles.segment_definitions (
 DisplayName,
 DomainName,
 SegmentDefinitionName,
 SegmentGroups,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ DomainName }}',
 '{{ SegmentDefinitionName }}',
 '{{ SegmentGroups }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.customerprofiles.segment_definitions (
 Description,
 DisplayName,
 DomainName,
 SegmentDefinitionName,
 SegmentGroups,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ DomainName }}',
 '{{ SegmentDefinitionName }}',
 '{{ SegmentGroups }}',
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
  - name: segment_definition
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: SegmentDefinitionName
        value: '{{ SegmentDefinitionName }}'
      - name: SegmentGroups
        value:
          Groups:
            - Dimensions:
                - null
              SourceSegments:
                - SegmentDefinitionName: '{{ SegmentDefinitionName }}'
              SourceType: '{{ SourceType }}'
              Type: null
          Include: null
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
DELETE FROM aws.customerprofiles.segment_definitions
WHERE data__Identifier = '<DomainName|SegmentDefinitionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>segment_definitions</code> resource, the following permissions are required:

### Create
```json
profile:CreateSegmentDefinition,
profile:TagResource
```

### Read
```json
profile:GetSegmentDefinition
```

### Update
```json
profile:GetSegmentDefinition,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteSegmentDefinition
```

### List
```json
profile:ListSegmentDefinitions
```
