---
title: locations_billing_specs
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_billing_specs
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>locations_billing_specs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_billing_specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.locations_billing_specs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingResources" /> | `array` | The billing and managed disk billing resources for a region. |
| <CopyableCode code="vmSizeFilters" /> | `array` | The virtual machine filtering mode. Effectively this can enabling or disabling the virtual machine sizes in a particular set. |
| <CopyableCode code="vmSizeProperties" /> | `array` | The vm size properties. |
| <CopyableCode code="vmSizes" /> | `array` | The virtual machine sizes to include or exclude. |
| <CopyableCode code="vmSizesWithEncryptionAtHost" /> | `array` | The vm sizes which enable encryption at host. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists the billingSpecs for the specified subscription and location. |

## `SELECT` examples

Lists the billingSpecs for the specified subscription and location.


```sql
SELECT
billingResources,
vmSizeFilters,
vmSizeProperties,
vmSizes,
vmSizesWithEncryptionAtHost
FROM azure.hdinsight.locations_billing_specs
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```