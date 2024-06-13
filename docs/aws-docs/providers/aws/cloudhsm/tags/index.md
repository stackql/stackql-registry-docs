---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - cloudhsm
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

Contains a tag. A tag is a key-value pair.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a tag. A tag is a key-value pair.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudhsm.tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The key of the tag.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>The value of the tag.</td></tr>
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
    <td><CopyableCode code="list_tags" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ResourceId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="tag_resource" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ResourceId, data__TagList, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="untag_resource" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ResourceId, data__TagKeyList, region" /></td>
  </tr>
</tbody></table>








