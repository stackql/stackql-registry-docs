---
title: partner
hide_title: false
hide_table_of_contents: false
keywords:
  - partner
  - cloudcontrolspartner
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

Creates, updates, deletes, gets or lists a <code>partner</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.partner" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the partner. Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner" |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the resource was created |
| <CopyableCode code="ekmSolutions" /> | `array` | List of Google Cloud supported EKM partners supported by the partner |
| <CopyableCode code="operatedCloudRegions" /> | `array` | List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: https://cloud.google.com/compute/docs/regions-zones |
| <CopyableCode code="partnerProjectId" /> | `string` | Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners. |
| <CopyableCode code="skus" /> | `array` | List of SKUs the partner is offering |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the resource was updated |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_partner" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Get details of a Partner. |

## `SELECT` examples

Get details of a Partner.

```sql
SELECT
name,
createTime,
ekmSolutions,
operatedCloudRegions,
partnerProjectId,
skus,
updateTime
FROM google.cloudcontrolspartner.partner
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```
