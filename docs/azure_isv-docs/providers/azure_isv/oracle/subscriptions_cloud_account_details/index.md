---
title: subscriptions_cloud_account_details
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_cloud_account_details
  - oracle
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

Creates, updates, deletes, gets or lists a <code>subscriptions_cloud_account_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_cloud_account_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.subscriptions_cloud_account_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloudAccountHomeRegion" /> | `string` | Cloud Account Home region |
| <CopyableCode code="cloudAccountName" /> | `string` | Cloud Account name |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Cloud Account Details |

## `SELECT` examples

List Cloud Account Details


```sql
SELECT
cloudAccountHomeRegion,
cloudAccountName
FROM azure_isv.oracle.subscriptions_cloud_account_details
WHERE subscriptionId = '{{ subscriptionId }}';
```