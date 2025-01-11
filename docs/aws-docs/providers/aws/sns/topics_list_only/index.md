---
title: topics_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - topics_list_only
  - sns
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

Lists <code>topics</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/topics/"><code>topics</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SNS::Topic</code> resource creates a topic to which notifications can be published.<br />One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see &#91;endpoints and quotas&#93;(https://docs.aws.amazon.com/general/latest/gr/sns.html) in the *General Reference*.<br />The structure of <code>AUTHPARAMS</code> depends on the .signature of the API request. For more information, see &#91;Examples of the complete Signature Version 4 signing process&#93;(https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sns.topics_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="topic_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>topics</code> in a region.
```sql
SELECT
region,
topic_arn
FROM aws.sns.topics_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>topics_list_only</code> resource, see <a href="/providers/aws/sns/topics/#permissions"><code>topics</code></a>

