--!strict
local MessagingService = game:GetService("MessagingService")
local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")

print("Starting rolink...")

local success, err = pcall(function()
	MessagingService:SubscribeAsync("rolink", function(message)
		local ok, data = pcall(function()
			return HttpService:JSONDecode(message.Data)
		end)
		
		if not ok or type(data) ~= "table" or type(data.command) ~= "string" then
			return
		end
		
		local command = data.command
		local args = data.args or {}
		local target_name = args.target
		
		if type(target_name) ~= "string" then return end -- erm

		if command == "kick" then
			for _, player in Players:GetPlayers() do
				if string.lower(player.Name) == string.lower(target_name) then
					player:Kick(args.reason or "You have been kicked")
					break
				end
			end
		elseif command == "ban" then
			local ok_id, user_id = pcall(function()
				return Players:GetUserIdFromNameAsync(target_name)
			end)
			if not ok_id or not user_id then return end
			
			local ban_ok, ban_err = pcall(function()
				Players:BanAsync({
					UserIds = { user_id },
					Duration = tonumber(args.seconds) or -1,
					DisplayReason = args.reason or "You have been banned",
					PrivateReason = "Banned via command",
					ExcludeAltAccounts = not args.ban_alts,
					ApplyToUniverse = true
				})
			end)
			if not ban_ok then
				warn("Rolink error: ", ban_err)
			end
		end
	end)
end)

if not success then
	warn("Rolink failed 2 connect: ", err)
else
	print("Rolink connected")
end
 
