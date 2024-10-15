---
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principals
  - automanage
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

Creates, updates, deletes, gets or lists a <code>service_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.service_principals" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Service Principal properties for the subscription. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the Automanage AAD first party Application Service Principal details for the subscription id. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the Automanage AAD first party Application Service Principal details for the subscription id. |

## `SELECT` examples

Get the Automanage AAD first party Application Service Principal details for the subscription id.


```sql
SELECT
properties,
systemData
FROM azure.automanage.service_principals
WHERE subscriptionId = '{{ subscriptionId }}';
```