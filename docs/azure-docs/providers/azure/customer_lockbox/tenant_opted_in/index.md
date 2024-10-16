---
title: tenant_opted_in
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_opted_in
  - customer_lockbox
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

Creates, updates, deletes, gets or lists a <code>tenant_opted_in</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_opted_in</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.tenant_opted_in" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="isOptedIn" /> | `boolean` | True if tenant is opted in, false otherwise |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="tenantId" /> | Get Customer Lockbox request |

## `SELECT` examples

Get Customer Lockbox request


```sql
SELECT
isOptedIn
FROM azure.customer_lockbox.tenant_opted_in
WHERE tenantId = '{{ tenantId }}';
```