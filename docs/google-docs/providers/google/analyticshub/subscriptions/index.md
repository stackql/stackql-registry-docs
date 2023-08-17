---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - analyticshub
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the subscription. e.g. `projects/myproject/locations/US/subscriptions/123`. |
| `state` | `string` | Output only. Current state of the subscription. |
| `subscriberContact` | `string` | Output only. Email of the subscriber. |
| `linkedDatasetMap` | `object` | Output only. Map of listing resource names to associated linked resource, e.g. projects/123/locations/US/dataExchanges/456/listings/789 -&gt; projects/123/datasets/my_dataset For listing-level subscriptions, this is a map of size 1. Only contains values if state == STATE_ACTIVE. |
| `creationTime` | `string` | Output only. Timestamp when the subscription was created. |
| `listing` | `string` | Output only. Resource name of the source Listing. e.g. projects/123/locations/US/dataExchanges/456/listings/789 |
| `organizationDisplayName` | `string` | Output only. Display name of the project of this subscription. |
| `lastModifyTime` | `string` | Output only. Timestamp when the subscription was last modified. |
| `dataExchange` | `string` | Output only. Resource name of the source Data Exchange. e.g. projects/123/locations/US/dataExchanges/456 |
| `organizationId` | `string` | Output only. Organization of the project this subscription belongs to. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_subscriptions_list` | `SELECT` | `locationsId, projectsId` | Lists all subscriptions in a given project and location. |
| `projects_locations_subscriptions_delete` | `DELETE` | `locationsId, projectsId, subscriptionsId` | Deletes a subscription. |
| `_projects_locations_subscriptions_list` | `EXEC` | `locationsId, projectsId` | Lists all subscriptions in a given project and location. |
| `projects_locations_subscriptions_get` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Gets the details of a Subscription. |
| `projects_locations_subscriptions_refresh` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets. |
| `projects_locations_subscriptions_revoke` | `EXEC` | `locationsId, projectsId, subscriptionsId` | Revokes a given subscription. |
