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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.serviceusage.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="services" /> | `array` | The requested Service states. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="batch_get" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Returns the service configurations and enabled states for a given list of services. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Returns the service configuration and enabled state for a given service. |
| <CopyableCode code="batch_enable" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Enable multiple services on a project. The operation is atomic: if enabling any service fails, then the entire batch fails, and no state changes occur. To enable a single service, use the `EnableService` method instead. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="name" /> | Disable a service so that it can no longer be used with a project. This prevents unintended usage that may cause unexpected billing charges or security leaks. It is not valid to call the disable method on a service that is not currently enabled. Callers will receive a `FAILED_PRECONDITION` status if the target service is not currently enabled. |

## `SELECT` examples

Returns the service configuration and enabled state for a given service.

```sql
SELECT
services
FROM google.serviceusage.services
WHERE name = '{{ name }}'; 
```
