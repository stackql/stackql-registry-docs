---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - load_balancers
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.load_balancers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a load balancer. |
| <CopyableCode code="name" /> | `string` | A human-readable name for a load balancer instance. |
| <CopyableCode code="algorithm" /> | `string` | This field has been deprecated. You can no longer specify an algorithm for load balancers. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the load balancer was created. |
| <CopyableCode code="disable_lets_encrypt_dns_records" /> | `boolean` | A boolean value indicating whether to disable automatic DNS record creation for Let's Encrypt certificates that are added to the load balancer. |
| <CopyableCode code="droplet_ids" /> | `array` | An array containing the IDs of the Droplets assigned to the load balancer. |
| <CopyableCode code="enable_backend_keepalive" /> | `boolean` | A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets. |
| <CopyableCode code="enable_proxy_protocol" /> | `boolean` | A boolean value indicating whether PROXY Protocol is in use. |
| <CopyableCode code="firewall" /> | `object` | An object specifying allow and deny rules to control traffic to the load balancer. |
| <CopyableCode code="forwarding_rules" /> | `array` | An array of objects specifying the forwarding rules for a load balancer. |
| <CopyableCode code="health_check" /> | `object` | An object specifying health check settings for the load balancer. |
| <CopyableCode code="http_idle_timeout_seconds" /> | `integer` | An integer value which configures the idle timeout for HTTP requests to the target droplets. |
| <CopyableCode code="ip" /> | `string` | An attribute containing the public-facing IP address of the load balancer. |
| <CopyableCode code="project_id" /> | `string` | The ID of the project that the load balancer is associated with. If no ID is provided at creation, the load balancer associates with the user's default project. If an invalid project ID is provided, the load balancer will not be created. |
| <CopyableCode code="redirect_http_to_https" /> | `boolean` | A boolean value indicating whether HTTP requests to the load balancer on port 80 will be redirected to HTTPS on port 443. |
| <CopyableCode code="region" /> | `object` | The region where the load balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a load balancer, an entire region object will be returned. |
| <CopyableCode code="size" /> | `string` | This field has been replaced by the `size_unit` field for all regions except in AMS2, NYC2, and SFO1. Each available load balancer size now equates to the load balancer having a set number of nodes.<br />* `lb-small` = 1 node<br />* `lb-medium` = 3 nodes<br />* `lb-large` = 6 nodes<br /><br />You can resize load balancers after creation up to once per hour. You cannot resize a load balancer within the first hour of its creation. |
| <CopyableCode code="size_unit" /> | `integer` | How many nodes the load balancer contains. Each additional node increases the load balancer's ability to manage more connections. Load balancers can be scaled up or down, and you can change the number of nodes after creation up to once per hour. This field is currently not available in the AMS2, NYC2, or SFO1 regions. Use the `size` field to scale load balancers that reside in these regions. |
| <CopyableCode code="status" /> | `string` | A status string indicating the current state of the load balancer. This can be `new`, `active`, or `errored`. |
| <CopyableCode code="sticky_sessions" /> | `object` | An object specifying sticky sessions settings for the load balancer. |
| <CopyableCode code="tag" /> | `string` | The name of a Droplet tag corresponding to Droplets assigned to the load balancer. |
| <CopyableCode code="vpc_uuid" /> | `string` | A string specifying the UUID of the VPC to which the load balancer is assigned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="loadBalancers_get" /> | `SELECT` | <CopyableCode code="lb_id" /> | To show information about a load balancer instance, send a GET request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID`.<br /> |
| <CopyableCode code="loadBalancers_list" /> | `SELECT` |  | To list all of the load balancer instances on your account, send a GET request<br />to `/v2/load_balancers`.<br /> |
| <CopyableCode code="loadBalancers_create" /> | `INSERT` |  | To create a new load balancer instance, send a POST request to<br />`/v2/load_balancers`.<br /><br />You can specify the Droplets that will sit behind the load balancer using one<br />of two methods:<br /><br />* Set `droplet_ids` to a list of specific Droplet IDs.<br />* Set `tag` to the name of a tag. All Droplets with this tag applied will be<br />  assigned to the load balancer. Additional Droplets will be automatically<br />  assigned as they are tagged.<br /><br />These methods are mutually exclusive.<br /> |
| <CopyableCode code="loadBalancers_delete" /> | `DELETE` | <CopyableCode code="lb_id" /> | To delete a load balancer instance, disassociating any Droplets assigned to it<br />and removing it from your account, send a DELETE request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| <CopyableCode code="_loadBalancers_get" /> | `EXEC` | <CopyableCode code="lb_id" /> | To show information about a load balancer instance, send a GET request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID`.<br /> |
| <CopyableCode code="_loadBalancers_list" /> | `EXEC` |  | To list all of the load balancer instances on your account, send a GET request<br />to `/v2/load_balancers`.<br /> |
| <CopyableCode code="loadBalancers_update" /> | `EXEC` | <CopyableCode code="lb_id" /> | To update a load balancer's settings, send a PUT request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full<br />representation of the load balancer including existing attributes. It may<br />contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually<br />exclusive. **Note that any attribute that is not provided will be reset to its<br />default value.**<br /> |
