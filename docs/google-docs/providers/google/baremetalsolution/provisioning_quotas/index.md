---
title: provisioning_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_quotas
  - baremetalsolution
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

Creates, updates, deletes or gets an <code>provisioning_quota</code> resource or lists <code>provisioning_quotas</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.provisioning_quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the provisioning quota. |
| <CopyableCode code="assetType" /> | `string` | The asset type of this provisioning quota. |
| <CopyableCode code="availableCount" /> | `integer` | The available count of the provisioning quota. |
| <CopyableCode code="gcpService" /> | `string` | The gcp service of the provisioning quota. |
| <CopyableCode code="instanceQuota" /> | `object` | A resource budget. |
| <CopyableCode code="location" /> | `string` | The specific location of the provisioining quota. |
| <CopyableCode code="networkBandwidth" /> | `string` | Network bandwidth, Gbps |
| <CopyableCode code="serverCount" /> | `string` | Server count. |
| <CopyableCode code="storageGib" /> | `string` | Storage size (GB). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List the budget details to provision resources on a given project. |

## `SELECT` examples

List the budget details to provision resources on a given project.

```sql
SELECT
name,
assetType,
availableCount,
gcpService,
instanceQuota,
location,
networkBandwidth,
serverCount,
storageGib
FROM google.baremetalsolution.provisioning_quotas
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
