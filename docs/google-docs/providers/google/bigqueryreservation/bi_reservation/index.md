---
title: bi_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - bi_reservation
  - bigqueryreservation
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
<tr><td><b>Name</b></td><td><code>bi_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigqueryreservation.bi_reservation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the singleton BI reservation. Reservation names have the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/biReservation`. |
| <CopyableCode code="preferredTables" /> | `array` | Preferred tables to use BI capacity for. |
| <CopyableCode code="size" /> | `string` | Size of a reservation, in bytes. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_bi_reservation" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Retrieves a BI reservation. |
| <CopyableCode code="update_bi_reservation" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Updates a BI reservation. Only fields specified in the `field_mask` are updated. A singleton BI reservation always exists with default size 0. In order to reserve BI capacity it needs to be updated to an amount greater than 0. In order to release BI capacity reservation size must be set to 0. |
