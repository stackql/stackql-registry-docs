---
title: fhir_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_destinations
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>fhir_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.fhir_destinations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | IoT Connector destination properties for an Azure FHIR service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_iot_connector" /> | `SELECT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all FHIR destinations for the given IoT Connector |

## `SELECT` examples

Lists all FHIR destinations for the given IoT Connector


```sql
SELECT
location,
properties,
systemData
FROM azure_extras.healthcare.fhir_destinations
WHERE iotConnectorName = '{{ iotConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```