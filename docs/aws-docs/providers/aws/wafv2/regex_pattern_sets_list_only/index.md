---
title: regex_pattern_sets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - regex_pattern_sets_list_only
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

Lists <code>regex_pattern_sets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/regex_pattern_sets/"><code>regex_pattern_sets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regex_pattern_sets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.regex_pattern_sets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the RegexPatternSet.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the RegexPatternSet</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>regex_pattern_sets</code> in a region.
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.regex_pattern_sets_list_only
;
```


## Permissions

For permissions required to operate on the <code>regex_pattern_sets_list_only</code> resource, see <a href="/providers/aws/wafv2/regex_pattern_sets/#permissions"><code>regex_pattern_sets</code></a>

