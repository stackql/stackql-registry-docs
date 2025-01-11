---
title: hsm
hide_title: false
hide_table_of_contents: false
keywords:
  - hsm
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

Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hsm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hsm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudhsm.hsm" /></td></tr>
</tbody></table>

## Fields
<code>SELECT</code> operation not supported for this resource.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_hsm" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="X-Amz-Target, data__AvailabilityZone, data__ClusterId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_hsm" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ClusterId, region" /></td>
  </tr>
</tbody></table>






