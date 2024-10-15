---
title: fleets_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets_credentials
  - fleet
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

Creates, updates, deletes, gets or lists a <code>fleets_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.fleets_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kubeconfigs" /> | `array` | Array of base64-encoded Kubernetes configuration files. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Lists the user credentials of a Fleet. |

## `SELECT` examples

Lists the user credentials of a Fleet.


```sql
SELECT
kubeconfigs
FROM azure.fleet.fleets_credentials
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```