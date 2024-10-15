---
title: certificate_orders_diagnostics_app_service_certificate_order_detector_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_diagnostics_app_service_certificate_order_detector_responses
  - app_service
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

Creates, updates, deletes, gets or lists a <code>certificate_orders_diagnostics_app_service_certificate_order_detector_responses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_orders_diagnostics_app_service_certificate_order_detector_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.certificate_orders_diagnostics_app_service_certificate_order_detector_responses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DetectorResponse resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateOrderName, detectorName, resourceGroupName, subscriptionId" /> | Description for Microsoft.CertificateRegistration call to get a detector response from App Lens. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Microsoft.CertificateRegistration to get the list of detectors for this RP. |

## `SELECT` examples

Description for Microsoft.CertificateRegistration to get the list of detectors for this RP.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.certificate_orders_diagnostics_app_service_certificate_order_detector_responses
WHERE certificateOrderName = '{{ certificateOrderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```