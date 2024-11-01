---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - provider_integrations
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.provider_integrations.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_environment" /> | `` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="config" /> | `object` | Cloud provider specific configs for provider integration |
| <CopyableCode code="display_name" /> | `string` | Display name of Provider Integration. |
| <CopyableCode code="environment" /> | `object` | The environment to which this belongs. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="provider" /> | `string` | Cloud provider to which access is provided through provider integration. |
| <CopyableCode code="usages" /> | `array` | List of resource crns where this integration is being used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_pim_v1integration" /> | `SELECT` | <CopyableCode code="environment, id" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/badge/-Request%20Access%20To%20Provider%20Integration-%23bc8540)](mailto:ccloud-api-access+pim-v1-early-access@confluent.io?subject=Request%20to%20join%20pim/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20pim/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to read an integration. |
| <CopyableCode code="list_pim_v1integrations" /> | `SELECT` | <CopyableCode code="environment" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/badge/-Request%20Access%20To%20Provider%20Integration-%23bc8540)](mailto:ccloud-api-access+pim-v1-early-access@confluent.io?subject=Request%20to%20join%20pim/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20pim/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Retrieve a sorted, filtered, paginated list of all integrations.<br /><br />If no `provider` filter is specified, returns provider integrations from all clouds.<br /> |
| <CopyableCode code="create_pim_v1integration" /> | `INSERT` |  | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/badge/-Request%20Access%20To%20Provider%20Integration-%23bc8540)](mailto:ccloud-api-access+pim-v1-early-access@confluent.io?subject=Request%20to%20join%20pim/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20pim/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to create an integration. |
| <CopyableCode code="delete_pim_v1integration" /> | `DELETE` | <CopyableCode code="environment, id" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/badge/-Request%20Access%20To%20Provider%20Integration-%23bc8540)](mailto:ccloud-api-access+pim-v1-early-access@confluent.io?subject=Request%20to%20join%20pim/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20pim/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)<br /><br />Make a request to delete an integration.<br /><br />This request fails if existing workloads are using this CSP integration.<br /> |
