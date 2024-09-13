
---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - serviceusage
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

Creates, updates, deletes or gets an <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.serviceusage.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the consumer and service. A valid name would be: - projects/123/services/serviceusage.googleapis.com |
| <CopyableCode code="config" /> | `object` | The configuration of the service. |
| <CopyableCode code="parent" /> | `string` | The resource name of the consumer. A valid name would be: - projects/123 |
| <CopyableCode code="state" /> | `string` | Whether or not the service has been enabled for use by the consumer. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Returns the service configuration and enabled state for a given service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List all services available to the specified project, and the current state of those services with respect to the project. The list includes all public services, all services for which the calling user has the `servicemanagement.services.bind` permission, and all services that have already been enabled on the project. The list can be filtered to only include services in a specific state, for example to only include services enabled on the project. WARNING: If you need to query enabled services frequently or across an organization, you should use [Cloud Asset Inventory API](https://cloud.google.com/asset-inventory/docs/apis), which provides higher throughput and richer filtering capability. |
| <CopyableCode code="batch_enable" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Enable multiple services on a project. The operation is atomic: if enabling any service fails, then the entire batch fails, and no state changes occur. To enable a single service, use the `EnableService` method instead. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="name" /> | Enable a service so that it can be used with a project. |

## `SELECT` examples

Returns the service configuration and enabled state for a given service.

```sql
SELECT
name,
config,
parent,
state
FROM google.serviceusage.services
WHERE name = '{{ name }}'; 
```
