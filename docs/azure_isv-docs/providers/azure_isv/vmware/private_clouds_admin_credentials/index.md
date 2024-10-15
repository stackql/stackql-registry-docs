---
title: private_clouds_admin_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds_admin_credentials
  - vmware
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

Creates, updates, deletes, gets or lists a <code>private_clouds_admin_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_clouds_admin_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.private_clouds_admin_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nsxtPassword" /> | `string` | NSX-T Manager password |
| <CopyableCode code="nsxtUsername" /> | `string` | NSX-T Manager username |
| <CopyableCode code="vcenterPassword" /> | `string` | vCenter admin password |
| <CopyableCode code="vcenterUsername" /> | `string` | vCenter admin username |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
nsxtPassword,
nsxtUsername,
vcenterPassword,
vcenterUsername
FROM azure_isv.vmware.private_clouds_admin_credentials
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```