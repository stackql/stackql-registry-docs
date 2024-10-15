---
title: replication_eligibility_results
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_eligibility_results
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_eligibility_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_eligibility_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_eligibility_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets Unique ARM identifier for this object. |
| <CopyableCode code="name" /> | `string` | Gets the name of this object. |
| <CopyableCode code="properties" /> | `object` | Properties model for replication eligibility results API. |
| <CopyableCode code="type" /> | `string` | Gets the object type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Validates whether a given VM can be protected or not in which case returns list of errors. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Validates whether a given VM can be protected or not in which case returns list of errors. |

## `SELECT` examples

Validates whether a given VM can be protected or not in which case returns list of errors.


```sql
SELECT
id,
name,
properties,
type
FROM azure.recovery_services_site_recovery.replication_eligibility_results
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```