---
title: workloads_partner_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads_partner_permissions
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

Creates, updates, deletes, gets or lists a <code>workloads_partner_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workloads_partner_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads_partner_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions` |
| <CopyableCode code="partnerPermissions" /> | `array` | The partner permissions granted for the workload |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_partner_permissions" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Gets the partner permissions granted for a workload |

## `SELECT` examples

Gets the partner permissions granted for a workload

```sql
SELECT
name,
partnerPermissions
FROM google.cloudcontrolspartner.workloads_partner_permissions
WHERE customersId = '{{ customersId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}';
```
