---
title: tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - tenants
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.tenants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID of the tenant. For example, /tenants/00000000-0000-0000-0000-000000000000. |
| <CopyableCode code="country" /> | `string` | Country/region name of the address for the tenant. |
| <CopyableCode code="countryCode" /> | `string` | Country/region abbreviation for the tenant. |
| <CopyableCode code="defaultDomain" /> | `string` | The default domain for the tenant. |
| <CopyableCode code="displayName" /> | `string` | The display name of the tenant. |
| <CopyableCode code="domains" /> | `array` | The list of domains for the tenant. |
| <CopyableCode code="tenantBrandingLogoUrl" /> | `string` | The tenant's branding logo URL. Only available for 'Home' tenant category. |
| <CopyableCode code="tenantCategory" /> | `string` | Category of the tenant. |
| <CopyableCode code="tenantId" /> | `string` | The tenant ID. For example, 00000000-0000-0000-0000-000000000000. |
| <CopyableCode code="tenantType" /> | `string` | The tenant type. Only available for 'Home' tenant category. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets the tenants for your account. |

## `SELECT` examples

Gets the tenants for your account.


```sql
SELECT
id,
country,
countryCode,
defaultDomain,
displayName,
domains,
tenantBrandingLogoUrl,
tenantCategory,
tenantId,
tenantType
FROM azure.resources.tenants
;
```