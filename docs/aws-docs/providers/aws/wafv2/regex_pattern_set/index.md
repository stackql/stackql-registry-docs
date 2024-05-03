---
title: regex_pattern_set
hide_title: false
hide_table_of_contents: false
keywords:
  - regex_pattern_set
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

Gets or operates on an individual <code>regex_pattern_set</code> resource, use <code>regex_pattern_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regex_pattern_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.regex_pattern_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the WAF entity.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
arn,
description,
name,
id,
regular_expression_list,
scope,
tags
FROM aws.wafv2.regex_pattern_set
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```

## Permissions

To operate on the <code>regex_pattern_set</code> resource, the following permissions are required:

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

