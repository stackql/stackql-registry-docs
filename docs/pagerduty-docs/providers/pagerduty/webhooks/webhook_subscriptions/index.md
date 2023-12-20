---
title: webhook_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_subscriptions
  - webhooks
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
<tr><td><b>Name</b></td><td><code>webhook_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.webhooks.webhook_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` | A short description of the webhook subscription. |
| `active` | `boolean` | Determines whether this subscription will produce webhook events. |
| `delivery_method` | `object` |  |
| `events` | `array` | The set of outbound event types the webhook will receive. |
| `filter` | `object` |  |
| `type` | `string` | The type indicating the schema of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook_subscription` | `SELECT` | `id` | Gets details about an existing webhook subscription.<br /> |
| `list_webhook_subscriptions` | `SELECT` |  | List existing webhook subscriptions.<br /><br />The `filter_type` and `filter_id` query parameters may be used to only show subscriptions<br />for a particular _service_ or _team_.<br /><br />For more information on webhook subscriptions and how they are used to configure v3 webhooks<br />see the [Webhooks v3 Developer Documentation](https://developer.pagerduty.com/docs/webhooks/v3-overview/).<br /> |
| `create_webhook_subscription` | `INSERT` | `data__webhook_subscription` | Creates a new webhook subscription.<br /><br />For more information on webhook subscriptions and how they are used to configure v3 webhooks<br />see the [Webhooks v3 Developer Documentation](https://developer.pagerduty.com/docs/webhooks/v3-overview/).<br /> |
| `delete_webhook_subscription` | `DELETE` | `id` | Deletes a webhook subscription.<br /> |
| `_get_webhook_subscription` | `EXEC` | `id` | Gets details about an existing webhook subscription.<br /> |
| `_list_webhook_subscriptions` | `EXEC` |  | List existing webhook subscriptions.<br /><br />The `filter_type` and `filter_id` query parameters may be used to only show subscriptions<br />for a particular _service_ or _team_.<br /><br />For more information on webhook subscriptions and how they are used to configure v3 webhooks<br />see the [Webhooks v3 Developer Documentation](https://developer.pagerduty.com/docs/webhooks/v3-overview/).<br /> |
| `enable_webhook_subscription` | `EXEC` | `id` | Enable a webhook subscription that is temporarily disabled. (This API does not require a request body.)<br /><br />Webhook subscriptions can become temporarily disabled when the subscription's delivery method is repeatedly rejected by the server.<br /> |
| `test_webhook_subscription` | `EXEC` | `id` | Test a webhook subscription.<br /><br />Fires a test event against the webhook subscription.  If properly configured,<br />this will deliver the `pagey.ping` webhook event to the destination.<br /> |
| `update_webhook_subscription` | `EXEC` | `id` | Updates an existing webhook subscription.<br /><br />Only the fields being updated need to be included on the request.  This operation does not<br />support updating the `delivery_method` of the webhook subscription.<br /> |
