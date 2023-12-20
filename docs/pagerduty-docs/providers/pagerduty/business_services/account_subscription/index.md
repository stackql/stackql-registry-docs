---
title: account_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - account_subscription
  - business_services
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.business_services.account_subscription</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `create_business_service_account_subscription` | `INSERT` | `id` | Subscribe your Account to a Business Service.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| `remove_business_service_account_subscription` | `DELETE` | `id` | Unsubscribe your Account from a Business Service.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| `remove_business_service_notification_subscriber` | `EXEC` | `id, data__subscribers` | Unsubscribes the matching Subscribers from a Business Service.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
