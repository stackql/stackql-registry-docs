---
title: data_exchanges_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exchanges_subscriptions
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
<tr><td><b>Name</b></td><td><code>data_exchanges_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.data_exchanges_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the subscription. e.g. `projects/myproject/locations/US/subscriptions/123`. |
| `organizationDisplayName` | `string` | Output only. Display name of the project of this subscription. |
| `creationTime` | `string` | Output only. Timestamp when the subscription was created. |
| `subscriberContact` | `string` | Output only. Email of the subscriber. |
| `linkedDatasetMap` | `object` | Output only. Map of listing resource names to associated linked resource, e.g. projects/123/locations/US/dataExchanges/456/listings/789 -&gt; projects/123/datasets/my_dataset For listing-level subscriptions, this is a map of size 1. Only contains values if state == STATE_ACTIVE. |
| `state` | `string` | Output only. Current state of the subscription. |
| `organizationId` | `string` | Output only. Organization of the project this subscription belongs to. |
| `lastModifyTime` | `string` | Output only. Timestamp when the subscription was last modified. |
| `dataExchange` | `string` | Output only. Resource name of the source Data Exchange. e.g. projects/123/locations/US/dataExchanges/456 |
| `listing` | `string` | Output only. Resource name of the source Listing. e.g. projects/123/locations/US/dataExchanges/456/listings/789 |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_data_exchanges_list_subscriptions` | `SELECT` | `dataExchangesId, locationsId, projectsId` |
| `_projects_locations_data_exchanges_list_subscriptions` | `EXEC` | `dataExchangesId, locationsId, projectsId` |
