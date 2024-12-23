---
title: balance
hide_title: false
hide_table_of_contents: false
keywords:
  - balance
  - apigee
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>balance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.balance" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_balance_adjust" /> | `EXEC` | <CopyableCode code="developersId, organizationsId" /> | Adjust the prepaid balance for the developer. This API will be used in scenarios where the developer has been under-charged or over-charged. |
| <CopyableCode code="organizations_developers_balance_credit" /> | `EXEC` | <CopyableCode code="developersId, organizationsId" /> | Credits the account balance for the developer. |
