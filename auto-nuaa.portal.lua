nuaaSSID = "nuaa.portal"
lastSSID = hs.wifi.currentNetwork()
function ssidChangedCallback()
    newSSID = hs.wifi.currentNetwork()
    if newSSID == nuaaSSID then
        command = "<directory of Python> '<directory of login.py>'"
        local handle = io.popen(command)
        local result = handle:read("*a")
        handle:close()
        hs.notify.new({title="Hammerspoon", informativeText=result}):send()
    end  
    lastSSID = newSSID
end
wifiWatcher = hs.wifi.watcher.new(ssidChangedCallback)
wifiWatcher:start()