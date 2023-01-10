---
title: workload_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks
  - vmware
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.workload_networks</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `WorkloadNetworks_CreateDhcp` | `EXEC` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_CreateDnsService` | `EXEC` | `dnsServiceId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_CreateDnsZone` | `EXEC` | `dnsZoneId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_CreatePortMirroring` | `EXEC` | `portMirroringId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_CreatePublicIP` | `EXEC` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_CreateSegments` | `EXEC` | `privateCloudName, resourceGroupName, segmentId, subscriptionId` |
| `WorkloadNetworks_CreateVMGroup` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId, vmGroupId` |
| `WorkloadNetworks_DeleteDhcp` | `EXEC` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_DeleteDnsService` | `EXEC` | `dnsServiceId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_DeleteDnsZone` | `EXEC` | `dnsZoneId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_DeletePortMirroring` | `EXEC` | `portMirroringId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_DeletePublicIP` | `EXEC` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_DeleteSegment` | `EXEC` | `privateCloudName, resourceGroupName, segmentId, subscriptionId` |
| `WorkloadNetworks_DeleteVMGroup` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId, vmGroupId` |
| `WorkloadNetworks_GetDhcp` | `EXEC` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetDnsService` | `EXEC` | `dnsServiceId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetDnsZone` | `EXEC` | `dnsZoneId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetGateway` | `EXEC` | `gatewayId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetPortMirroring` | `EXEC` | `portMirroringId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetPublicIP` | `EXEC` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_GetSegment` | `EXEC` | `privateCloudName, resourceGroupName, segmentId, subscriptionId` |
| `WorkloadNetworks_GetVMGroup` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId, vmGroupId` |
| `WorkloadNetworks_GetVirtualMachine` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId, virtualMachineId` |
| `WorkloadNetworks_ListDhcp` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListDnsServices` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListDnsZones` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListGateways` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListPortMirroring` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListPublicIPs` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListSegments` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListVMGroups` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_ListVirtualMachines` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_UpdateDhcp` | `EXEC` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_UpdateDnsService` | `EXEC` | `dnsServiceId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_UpdateDnsZone` | `EXEC` | `dnsZoneId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_UpdatePortMirroring` | `EXEC` | `portMirroringId, privateCloudName, resourceGroupName, subscriptionId` |
| `WorkloadNetworks_UpdateSegments` | `EXEC` | `privateCloudName, resourceGroupName, segmentId, subscriptionId` |
| `WorkloadNetworks_UpdateVMGroup` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId, vmGroupId` |
