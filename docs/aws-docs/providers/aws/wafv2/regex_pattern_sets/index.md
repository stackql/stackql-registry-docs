---
title: regex_pattern_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - regex_pattern_sets
  - wafv2
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

Creates, updates, deletes or gets a <code>regex_pattern_set</code> resource or lists <code>regex_pattern_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regex_pattern_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.regex_pattern_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the WAF entity.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the entity.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the RegexPatternSet.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the RegexPatternSet</td></tr>
<tr><td><CopyableCode code="regular_expression_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Scope, RegularExpressionList, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>regex_pattern_sets</code> in a region.
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.regex_pattern_sets
;
```
Gets all properties from a <code>regex_pattern_set</code>.
```sql
SELECT
region,
arn,
description,
name,
id,
regular_expression_list,
scope,
tags
FROM aws.wafv2.regex_pattern_sets
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>regex_pattern_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wafv2.regex_pattern_sets (
 RegularExpressionList,
 Scope,
 region
)
SELECT 
'{{ RegularExpressionList }}',
 '{{ Scope }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wafv2.regex_pattern_sets (
 Description,
 Name,
 RegularExpressionList,
 Scope,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ RegularExpressionList }}',
 '{{ Scope }}',
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
  - name: regex_pattern_set
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: RegularExpressionList
        value:
          - '{{ RegularExpressionList[0] }}'
      - name: Scope
        value: '{{ Scope }}'
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
DELETE FROM aws.wafv2.regex_pattern_sets
WHERE data__Identifier = '<Name|Id|Scope>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>regex_pattern_sets</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateRegexPatternSet,
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource
```

### Delete
```json
wafv2:DeleteRegexPatternSet,
wafv2:GetRegexPatternSet
```

### Read
```json
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateRegexPatternSet,
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource
```

### List
```json
wafv2:listRegexPatternSets
```

