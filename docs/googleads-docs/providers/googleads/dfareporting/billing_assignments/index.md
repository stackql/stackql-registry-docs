---
title: billing_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_assignments
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.billing_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `billingAssignments` | `array` | Billing assignments collection. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#billingAssignmentsListResponse". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAssignments_list` | `SELECT` | `billingProfileId, profileId` | Retrieves a list of billing assignments. |
| `billingAssignments_insert` | `EXEC` | `billingProfileId, profileId` | Inserts a new billing assignment and returns the new assignment. Only one of advertiser_id or campaign_id is support per request. If the new assignment has no effect (assigning a campaign to the parent advertiser billing profile or assigning an advertiser to the account billing profile), no assignment will be returned. |
