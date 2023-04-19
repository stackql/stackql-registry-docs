---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
  - droplets
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.droplets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation. |
| `name` | `string` | The human-readable name set for the Droplet instance. |
| `size` | `object` |  |
| `image` | `object` |  |
| `memory` | `integer` | Memory of the Droplet in megabytes. |
| `kernel` | `object` | **Note**: All Droplets created after March 2017 use internal kernels by default.<br />These Droplets will have this attribute set to `null`.<br /><br />The current [kernel](https://www.digitalocean.com/docs/droplets/how-to/kernel/)<br />for Droplets with externally managed kernels. This will initially be set to<br />the kernel of the base image when the Droplet is created.<br /> |
| `vpc_uuid` | `string` | A string specifying the UUID of the VPC to which the Droplet is assigned. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the Droplet was created. |
| `backup_ids` | `array` | An array of backup IDs of any backups that have been taken of the Droplet instance.  Droplet backups are enabled at the time of the instance creation. |
| `features` | `array` | An array of features enabled on this Droplet. |
| `tags` | `array` | An array of Tags the Droplet has been tagged with. |
| `locked` | `boolean` | A boolean value indicating whether the Droplet has been locked, preventing actions by users. |
| `size_slug` | `string` | The unique slug identifier for the size of this Droplet. |
| `snapshot_ids` | `array` | An array of snapshot IDs of any snapshots created from the Droplet instance. |
| `status` | `string` | A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive". |
| `disk` | `integer` | The size of the Droplet's disk in gigabytes. |
| `next_backup_window` | `object` | The details of the Droplet's backups feature, if backups are configured for the Droplet. This object contains keys for the start and end times of the window during which the backup will start. |
| `networks` | `object` | The details of the network that are configured for the Droplet instance.  This is an object that contains keys for IPv4 and IPv6.  The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet.  These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is. |
| `region` | `object` |  |
| `vcpus` | `integer` | The number of virtual CPUs. |
| `volume_ids` | `array` | A flat array including the unique identifier for each Block Storage volume attached to the Droplet. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `droplet_id` | To show information about an individual Droplet, send a GET request to<br />`/v2/droplets/$DROPLET_ID`.<br /> |
| `list` | `SELECT` |  | To list all Droplets in your account, send a GET request to `/v2/droplets`.<br /><br />The response body will be a JSON object with a key of `droplets`. This will be<br />set to an array containing objects each representing a Droplet. These will<br />contain the standard Droplet attributes.<br /><br />### Filtering Results by Tag<br /><br />It's possible to request filtered results by including certain query parameters.<br />To only list Droplets assigned to a specific tag, include the `tag_name` query<br />parameter set to the name of the tag in your GET request. For example,<br />`/v2/droplets?tag_name=$TAG_NAME`.<br /> |
| `create` | `INSERT` |  | To create a new Droplet, send a POST request to `/v2/droplets` setting the<br />required attributes.<br /><br />A Droplet will be created using the provided information. The response body<br />will contain a JSON object with a key called `droplet`. The value will be an<br />object containing the standard attributes for your new Droplet. The response<br />code, 202 Accepted, does not indicate the success or failure of the operation,<br />just that the request has been accepted for processing. The `actions` returned<br />as part of the response's `links` object can be used to check the status<br />of the Droplet create event.<br /><br />### Create Multiple Droplets<br /><br />Creating multiple Droplets is very similar to creating a single Droplet.<br />Instead of sending `name` as a string, send `names` as an array of strings. A<br />Droplet will be created for each name you send using the associated<br />information. Up to ten Droplets may be created this way at a time.<br /><br />Rather than returning a single Droplet, the response body will contain a JSON<br />array with a key called `droplets`. This will be set to an array of JSON<br />objects, each of which will contain the standard Droplet attributes. The<br />response code, 202 Accepted, does not indicate the success or failure of any<br />operation, just that the request has been accepted for processing. The array<br />of `actions` returned as part of the response's `links` object can be used to<br />check the status of each individual Droplet create event.<br /> |
| `_get` | `EXEC` | `droplet_id` | To show information about an individual Droplet, send a GET request to<br />`/v2/droplets/$DROPLET_ID`.<br /> |
| `_list` | `EXEC` |  | To list all Droplets in your account, send a GET request to `/v2/droplets`.<br /><br />The response body will be a JSON object with a key of `droplets`. This will be<br />set to an array containing objects each representing a Droplet. These will<br />contain the standard Droplet attributes.<br /><br />### Filtering Results by Tag<br /><br />It's possible to request filtered results by including certain query parameters.<br />To only list Droplets assigned to a specific tag, include the `tag_name` query<br />parameter set to the name of the tag in your GET request. For example,<br />`/v2/droplets?tag_name=$TAG_NAME`.<br /> |
| `destroy` | `EXEC` | `droplet_id` | To delete a Droplet, send a DELETE request to `/v2/droplets/$DROPLET_ID`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| `destroy_byTag` | `EXEC` | `tag_name` | To delete **all** Droplets assigned to a specific tag, include the `tag_name`<br />query parameter set to the name of the tag in your DELETE request. For<br />example,  `/v2/droplets?tag_name=$TAG_NAME`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| `destroy_retryWithAssociatedResources` | `EXEC` | `droplet_id` | If the status of a request to destroy a Droplet with its associated resources<br />reported any errors, it can be retried by sending a POST request to the<br />`/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/retry` endpoint.<br /><br />Only one destroy can be active at a time per Droplet. If a retry is issued<br />while another destroy is in progress for the Droplet a 409 status code will<br />be returned. A successful response will include a 202 response code and no<br />content.<br /> |
| `destroy_withAssociatedResourcesDangerous` | `EXEC` | `X-Dangerous, droplet_id` | To destroy a Droplet along with all of its associated resources, send a DELETE<br />request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/dangerous`<br />endpoint. The headers of this request must include an `X-Dangerous` key set to<br />`true`. To preview which resources will be destroyed, first query the<br />Droplet's associated resources. This operation _can not_ be reverse and should<br />be used with caution.<br /><br />A successful response will include a 202 response code and no content. Use the<br />status endpoint to check on the success or failure of the destruction of the<br />individual resources.<br /> |
| `destroy_withAssociatedResourcesSelective` | `EXEC` | `droplet_id` | To destroy a Droplet along with a sub-set of its associated resources, send a<br />DELETE request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/selective`<br />endpoint. The JSON body of the request should include `reserved_ips`, `snapshots`, `volumes`,<br />or `volume_snapshots` keys each set to an array of IDs for the associated<br />resources to be destroyed. The IDs can be found by querying the Droplet's<br />associated resources. Any associated resource not included in the request<br />will remain and continue to accrue changes on your account.<br /><br />A successful response will include a 202 response code and no content. Use<br />the status endpoint to check on the success or failure of the destruction of<br />the individual resources.<br /> |
| `get_DestroyAssociatedResourcesStatus` | `EXEC` | `droplet_id` | To check on the status of a request to destroy a Droplet with its associated<br />resources, send a GET request to the<br />`/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint.<br /> |
| `list_associatedResources` | `EXEC` | `droplet_id` | To list the associated billable resources that can be destroyed along with a<br />Droplet, send a GET request to the<br />`/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.<br /><br />The response will be a JSON object containing `snapshots`, `volumes`, and<br />`volume_snapshots` keys. Each will be set to an array of objects containing<br />information about the associated resources.<br /> |
| `list_neighborsIds` | `EXEC` |  | To retrieve a list of all Droplets that are co-located on the same physical<br />hardware, send a GET request to `/v2/reports/droplet_neighbors_ids`.<br /><br />The results will be returned as a JSON object with a key of `neighbor_ids`.<br />This will be set to an array of arrays. Each array will contain a set of<br />Droplet IDs for Droplets that share a physical server. An empty array<br />indicates that all Droplets associated with your account are located on<br />separate physical hardware.<br /> |
