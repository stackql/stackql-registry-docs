---
title: custom_host_name_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_host_name_analyses
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>custom_host_name_analyses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_host_name_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.custom_host_name_analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aRecords" /> | `array` | A records visible for this hostname. |
| <CopyableCode code="alternateCNameRecords" /> | `array` | Alternate CName records visible for this hostname. |
| <CopyableCode code="alternateTxtRecords" /> | `array` | Alternate TXT records visible for this hostname. |
| <CopyableCode code="cNameRecords" /> | `array` | CName records visible for this hostname. |
| <CopyableCode code="conflictWithEnvironmentCustomDomain" /> | `boolean` | <code>true</code> if there is a conflict on the Container App's managed environment level custom domain; otherwise, <code>false</code>. |
| <CopyableCode code="conflictingContainerAppResourceId" /> | `string` | Name of the conflicting Container App on the Managed Environment if it's within the same subscription. |
| <CopyableCode code="customDomainVerificationFailureInfo" /> | `object` | Raw failure information if DNS verification fails. |
| <CopyableCode code="customDomainVerificationTest" /> | `string` | DNS verification test result. |
| <CopyableCode code="hasConflictOnManagedEnvironment" /> | `boolean` | <code>true</code> if there is a conflict on the Container App's managed environment; otherwise, <code>false</code>. |
| <CopyableCode code="hostName" /> | `string` | Host name that was analyzed |
| <CopyableCode code="isHostnameAlreadyVerified" /> | `boolean` | <code>true</code> if hostname is already verified; otherwise, <code>false</code>. |
| <CopyableCode code="txtRecords" /> | `array` | TXT records visible for this hostname. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
aRecords,
alternateCNameRecords,
alternateTxtRecords,
cNameRecords,
conflictWithEnvironmentCustomDomain,
conflictingContainerAppResourceId,
customDomainVerificationFailureInfo,
customDomainVerificationTest,
hasConflictOnManagedEnvironment,
hostName,
isHostnameAlreadyVerified,
txtRecords
FROM azure.container_apps.custom_host_name_analyses
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```