---
title: resource_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_requests
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
<tr><td><b>Name</b></td><td><code>resource_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_requests</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloud_control.resource_requests" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource_requests" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__ResourceRequestStatusFilter, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="cancel_resource_request" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__RequestToken, region" /></td>
  </tr>
</tbody></table>






