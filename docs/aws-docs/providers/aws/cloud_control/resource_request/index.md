---
title: resource_request
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_request
  - cloud_control
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

For more information about Amazon Web Services Cloud Control API, see the <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html">Amazon Web Services Cloud Control API User Guide</a>.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_request</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloud_control.resource_request" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="error_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_time" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="operation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="operation_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="request_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_model" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retry_after" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource_request" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__RequestToken, region" /></td>
  </tr>
</tbody></table>








