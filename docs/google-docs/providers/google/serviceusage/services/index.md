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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="serviceusage.services" /></td></tr>
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
| <CopyableCode code="batch_enable" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Enable multiple services on a project. The operation is atomic: if enabling any service fails, then the entire batch fails, and no state changes occur. To enable a single service, use the `EnableService` method instead. |
| <CopyableCode code="batch_get" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Returns the service configurations and enabled states for a given list of services. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="name" /> | Enable a service so that it can be used with a project. |
