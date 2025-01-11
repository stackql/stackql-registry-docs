---
title: domain_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_tags
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

Expands all tag keys and values for <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.domain_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="dead_letter_queue_url" /></td><td><code>string</code></td><td>The URL of the SQS dead letter queue</td></tr>
<tr><td><CopyableCode code="default_encryption_key" /></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><CopyableCode code="default_expiration_days" /></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><CopyableCode code="matching" /></td><td><code>object</code></td><td>The process of matching duplicate profiles. If Matching = true, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. After the Identity Resolution Job completes, use the GetMatches API to return and review the results. Or, if you have configured ExportingConfig in the MatchingRequest, you can download the results from S3.</td></tr>
<tr><td><CopyableCode code="rule_based_matching" /></td><td><code>object</code></td><td>The process of matching duplicate profiles using the Rule-Based matching. If RuleBasedMatching = true, Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the RuleBasedMatchingRequest. You can use the ListRuleBasedMatches and GetSimilarProfiles API to return and review the results. Also, if you have configured ExportingConfig in the RuleBasedMatchingRequest, you can download the results from S3.</td></tr>
<tr><td><CopyableCode code="stats" /></td><td><code>object</code></td><td>Usage-specific statistics about the domain.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>domains</code> in a region.
```sql
SELECT
region,
domain_name,
dead_letter_queue_url,
default_encryption_key,
default_expiration_days,
matching,
rule_based_matching,
stats,
created_at,
last_updated_at,
tag_key,
tag_value
FROM aws.customerprofiles.domain_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domain_tags</code> resource, see <a href="/providers/aws/customerprofiles/domains/#permissions"><code>domains</code></a>

