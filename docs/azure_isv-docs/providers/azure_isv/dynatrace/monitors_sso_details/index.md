---
title: monitors_sso_details
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_sso_details
  - dynatrace
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

Creates, updates, deletes, gets or lists a <code>monitors_sso_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_sso_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_sso_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aadDomains" /> | `array` | array of Aad(azure active directory) domains |
| <CopyableCode code="adminUsers" /> | `array` | Array of admin user emails. |
| <CopyableCode code="isSsoEnabled" /> | `string` | Indicates whether SSO is enabled or not |
| <CopyableCode code="metadataUrl" /> | `string` | URL for Azure AD metadata |
| <CopyableCode code="singleSignOnUrl" /> | `string` | The login URL specific to this Dynatrace Environment |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userPrincipal" /> |  |

## `SELECT` examples




```sql
SELECT
aadDomains,
adminUsers,
isSsoEnabled,
metadataUrl,
singleSignOnUrl
FROM azure_isv.dynatrace.monitors_sso_details
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__userPrincipal = '{{ data__userPrincipal }}';
```